// @ts-nocheck
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import sitemap from '@astrojs/sitemap';
import fs from 'node:fs';
import path from 'node:path';
import { DISCORD_URL, GITHUB_URL, YOUTUBE_URL } from './src/site.config.mjs';
import redirects from './redirects.json' with { type: 'json' };

const isDev = process.argv.includes('dev');
const guidesDir = path.resolve('src/content/docs/guides');

// Read a guide file's front matter block.
function frontmatter(file) {
	return fs.readFileSync(file, 'utf8').split('---')[1] ?? '';
}

// Build A-Z sidebar groups from each guide's `game` front matter field.
// Flat guides become a single item; a guide folder with an `index` page becomes a
// group whose children are its sub-pages (e.g. chaos-zero-nightmare/{faugus,heroic}).
function guideGroups() {
	const items = [];
	const isDraft = (fm) => !isDev && /^draft:\s*true/m.test(fm);
	const gameOf = (fm, fallback) => fm.match(/^game:\s*"(.*)"/m)?.[1] ?? fallback;

	for (const entry of fs.readdirSync(guidesDir, { withFileTypes: true })) {
		if (entry.isFile() && /\.mdx?$/.test(entry.name)) {
			const fm = frontmatter(path.join(guidesDir, entry.name));
			if (isDraft(fm)) continue;
			items.push({ game: gameOf(fm, entry.name), slug: 'guides/' + entry.name.replace(/\.mdx?$/, '') });
		} else if (entry.isDirectory()) {
			const base = path.join(guidesDir, entry.name);
			const index = ['index.mdx', 'index.md'].map((f) => path.join(base, f)).find((f) => fs.existsSync(f));
			if (!index) continue;
			const fm = frontmatter(index);
			if (isDraft(fm)) continue;
			const children = [
				{ slug: 'guides/' + entry.name, label: 'Overview' },
				...fs
					.readdirSync(base)
					.filter((f) => /\.mdx?$/.test(f) && !/^index\.mdx?$/.test(f))
					.map((f) => {
						const sfm = frontmatter(path.join(base, f));
						const label = sfm.match(/^sidebar:\s*\n\s*label:\s*"(.*)"/m)?.[1] ?? sfm.match(/^title:\s*"(.*)"/m)?.[1] ?? f;
						return { draft: isDraft(sfm), slug: `guides/${entry.name}/${f.replace(/\.mdx?$/, '')}`, label };
					})
					.filter((c) => !c.draft)
					.map(({ draft, ...c }) => c),
			];
			items.push({ game: gameOf(fm, entry.name), slug: 'guides/' + entry.name, children });
		}
	}
	items.sort((a, b) => a.game.localeCompare(b.game));
	const groups = new Map();
	for (const it of items) {
		const first = it.game.replace(/^the\s+/i, '')[0].toUpperCase();
		const letter = /[A-Z]/.test(first) ? first : '#';
		if (!groups.has(letter)) groups.set(letter, []);
		const item = { slug: it.slug, label: it.game };
		if (it.children?.length) item.items = it.children;
		groups.get(letter).push(item);
	}
	return [...groups.entries()].map(([label, items]) => ({ label, items, collapsed: false }));
}

// Guides flagged `noindex: true` stay out of the sitemap (Head.astro adds the robots meta).
const noindexUrls = fs
	.readdirSync(guidesDir)
	.filter((f) => /\.mdx?$/.test(f) && /^noindex:\s*true/m.test(frontmatter(path.join(guidesDir, f))))
	.map((f) => `/guides/${f.replace(/\.mdx?$/, '')}/`);

export default defineConfig({
	site: process.env.SITE_URL || 'https://frostlinuxdev.github.io',
	redirects,
	integrations: [
		sitemap({ filter: (page) => !noindexUrls.some((u) => page.endsWith(u)) }),
		starlight({
			title: 'FrostLinux',
			customCss: ['./src/styles/custom.css'],
			components: {
				Head: './src/components/Head.astro',
				Header: './src/components/Header.astro',
				Footer: './src/components/Footer.astro',
				MarkdownContent: './src/components/MarkdownContent.astro',
			},
			description: 'Linux gaming guides for gacha games: Proton, Heroic, Steam and launcher setups.',
			social: [
				{ icon: 'youtube', label: 'YouTube', href: YOUTUBE_URL },
				...(GITHUB_URL ? [{ icon: 'github', label: 'GitHub', href: GITHUB_URL }] : []),
				...(DISCORD_URL ? [{ icon: 'discord', label: 'Discord', href: DISCORD_URL }] : []),
			],
			sidebar: [{ label: 'Guides', items: guideGroups() }],
		}),
	],
});

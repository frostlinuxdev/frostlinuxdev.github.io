import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
	const posts = (
		await getCollection(
			'docs',
			({ id, data }) => id.startsWith('news/') && !id.endsWith('/index') && !data.draft,
		)
	).sort((a, b) => (b.data.date?.valueOf() ?? 0) - (a.data.date?.valueOf() ?? 0));

	return rss({
		title: 'FrostLinux — News',
		description:
			'Steam releases, launch updates and other news for the gacha games covered on FrostLinux.',
		site: context.site ?? 'https://frostlinuxdev.github.io',
		items: posts.map((post) => ({
			title: post.data.title,
			description: post.data.description,
			pubDate: post.data.date,
			link: `/${post.id.replace(/\/index$/, '')}/`,
		})),
	});
}

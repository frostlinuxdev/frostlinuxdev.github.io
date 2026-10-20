import type { APIRoute } from 'astro';

// Generated so the sitemap URL always matches the deployed domain (`site`).
export const GET: APIRoute = ({ site }) => {
	const base = site ?? new URL('https://frostlinuxdev.github.io');
	const body = `User-agent: *\nAllow: /\n\nSitemap: ${new URL('sitemap-index.xml', base).href}\n`;
	return new Response(body, {
		headers: { 'Content-Type': 'text/plain; charset=utf-8' },
	});
};

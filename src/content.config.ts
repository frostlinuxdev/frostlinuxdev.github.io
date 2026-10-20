import { defineCollection, z } from 'astro:content';
import { docsLoader, i18nLoader } from '@astrojs/starlight/loaders';
import { docsSchema, i18nSchema } from '@astrojs/starlight/schema';

export const collections = {
	docs: defineCollection({
		loader: docsLoader(),
		schema: docsSchema({
			extend: z.object({
				date: z.coerce.date().optional(),
				author: z.string().optional(),
				category: z.string().optional(),
				game: z.string().optional(),
				image: z.string().optional(),
				heroImage: z.string().optional(),
				status: z
					.enum(['untested', 'drafted-from-video', 'works', 'needs-fix', 'broken'])
					.optional(),
				launcher: z.enum(['steam', 'heroic', 'faugus', 'lutris', 'twintail', 'heroic-or-faugus', '']).optional(),
				protonVersion: z.string().optional(),
				launcherName: z.string().optional(),
				hasGameplayVideo: z.boolean().optional(),
				gameplay: z.array(z.object({ id: z.string(), title: z.string() })).optional(),
				onSteam: z.boolean().optional(),
				website: z.string().url().optional(),
				protondbTier: z
					.enum(['platinum', 'gold', 'silver', 'bronze', 'borked'])
					.optional(),
				rating: z.enum(['out-of-the-box', 'custom-proton']).optional(),
				steamAppId: z.number().optional(),
				steamUrl: z.string().url().optional(),
				steamComingSoon: z.boolean().optional(),
				nadare: z.boolean().optional(),
				wip: z.boolean().optional(),
				noindex: z.boolean().optional(),
			}),
		}),
	}),
	i18n: defineCollection({ loader: i18nLoader(), schema: i18nSchema() }),
};

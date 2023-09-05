let char = 0xe000;

for (const namespace of ['twemoji', 'tinkerer']) {
	const font = {};
	font.providers = [];
	const style = {};

	for await (const f of Deno.readDir(`assets/${namespace}/textures/emoji`)) {
		const value = String.fromCodePoint(char++);
		font.providers.push({
			type: 'bitmap',
			file: `${namespace}:emoji/` + f.name,
			height: 9,
			ascent: 8,
			chars: [value],
		});

		style[f.name.substring(0, f.name.length - 4)] = `<font:'${namespace}:emoji'><white>${value}`;
	}

	Deno.writeTextFileSync(`assets/${namespace}/font/emoji.json`, JSON.stringify(font))
	Deno.writeTextFileSync(`${namespace}_emoji.json`, JSON.stringify(style))
}

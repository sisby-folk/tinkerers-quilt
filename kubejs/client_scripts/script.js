// priority: 0

console.info('Hello, World! (You will see this line every time client resources reload)')

onEvent('jei.hide.items', event => {
	// Hide items in JEI here
	// event.hide('minecraft:cobblestone')
})

onEvent('rei.information', event => {
	
  event.add('minecraft:slime_ball', 'Alternate Leaping', ['Slimeballs can be used to brew a potion of leaping from an awkward potion', 'This will leave a snowball in the slot'])
  event.add('minecraft:pufferfish_bucket', 'Alternate Water Breathing', ['Buckets of pufferfish can be used to brew a potion of water breathing from an awkward potion', 'The bucket of pufferfish will not be consumed.'])
})
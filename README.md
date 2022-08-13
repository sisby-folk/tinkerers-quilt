# Tinkerer's Quilt

------

<img float="right" style="float:right" width="100" height="100" src="https://user-images.githubusercontent.com/55819817/172377429-370926d7-2bb9-487b-9971-e63021e5a264.png" alt="Tinkerer's quilt logo. Kobold surrounded by quilt patches.">

**Tinkerer's Quilt**  (TQuilt) is a set of minecraft modpacks by Kapesi, Clawby, Herrah and Le'mer.     
Their design is centered on three pillars: **Vanilla Compatibility**, **Accessibility/UX**, and **Expression**

All packs run on Minecraft 1.18.2 and the **Quilt** mod loader

---

The three editions are as follows
- [Released] **Tinkerer's Quilt ("Base")** is the heart of all this. It's **Vanilla-World-Compatible**, with **no new items, blocks, or worldgen**. 
  - Designed to **teach you vanilla** through **fully in-game** quests and item info - you'll never need to open the wiki.
  - Built with a curated set of Quality of Life (QoL) improvements to ease the pains of vanilla.
  - **Easier than vanilla** with expressive origins, simplified enchanting/repair, and helpful quest rewards.

**Base** is designed to allow more experienced players to add extra mods.     
**Plus** and **Modded** is simply us doing exactly that - to our own tastes!    
The rest of this document focuses on Base, so here's a quick breakdown:

- [WIP] **Plus** is a Vanilla+ extension of base, including all of its quests.
  - Plus adds mods that expand on the **Godseeking** fields from base:
    - **Homesteading** - More farming/ranching, _way_ more cooking, more building blocks, and more decorations.
    - **Exploration** - More traversal options, new nether/end, new biomes, new structures, and a seasonal world.
    - **Combat** - Spears, chef's knives, and... compact mechanically propelled halfdoors? Plus new dungeons.
- [WIP] **Modded** a simple extension of plus, adding personal favourite major mods
  - Each mod is larger, with a complex progression equivalent to Base's **The Basics** tree, and then some.
  - **Botania** - Collect mana, power magic flowers, and study the elves in this beautifully simple magi-tech mod.
  - **Create** - Build steampunk masses of driveshafts, pistons, and conveyors in this larger-than-life old-tech mod.
  - **Tinker's Construct** - Though unstable on Quilt, TCon3 is our favourite tool/weapon system rework - ever.

---

# Installation

**Players**
 - Install [PolyMC](https://polymc.org/) and [Java 17](https://adoptium.net/temurin/releases/) (on Windows? choose `Windows-x64-JRE-17-.msi`)

   - Alternatively, run `winget install polymc` and `winget install --id EclipseAdoptium.TemurinJRE.17`.
   - [MultiMC](https://multimc.org/) is also supported on its _development_ branch. Swap to this in `settings-> launcher` and restart.

 - Download your preferred [Tinkerer's Quilt Version](https://sisby-folk.github.io/mc-packs/).

 - Drag and drop onto an open PolyMC/MultiMC window, press OK, and double click it to play!

   - When prompted for optional mods, press OK to continue, or customise to your liking first.
 
   - The pack will auto-update on every launch. To disable this, turn off **custom commands** in Edit Instance -> Settings.


**Server Hosts**:
 - Download a [TQuilt Server Version](https://sisby-folk.github.io/mc-packs/)
 - Run Quilt Installer and select `1.18.2` and the latest non-beta loader version. Then click "install"
 - Run `Update.bat` to install the pack, then `Start.bat` to run the server

---

# Pack Features

## Questing System
***"It's like FTB Academy for Vanilla!"*** - Us, just now

TQuilt's quests help guide old and new players through the core progression of minecraft, and explore all the way out the far reaches of what it has to offer.

### The Basics
      
<img width="425" height="260" src="https://user-images.githubusercontent.com/55819817/174097642-a5949541-b8e6-419b-bbfe-b3e4ecf90be8.png"><img width="325" height="260" src="https://user-images.githubusercontent.com/55819817/174098114-c5630f29-efaa-4473-9eb4-e53c4325f002.png">

Core game progression - get unfamiliar players on track, keep goals visible, and engage directly through tasks and rewards.

### Godseeking
Explore all parts of the game and many special interests - categorised by **Homesteading**, **Self-Defense**, and **Exploration**.   
Do you want to...
 - ⚔️ Know every weapon and kill every enemy? 
 - 🏠 Make bases in many environments? 
 - 🌾 farm anything and everything, including crops? 
 - 🗺️ Explore the world and what's found there? 
 - 🛠️ Craft the best gear in your own workshop? 
 - 🛣️ Build transit infrastructure and achieve ludicrous speed? 
 - ⚙️ Make terrifyingly complex machines and mechanisms? 

It's all there! Including things even we didn't know about before making this pack!     
These quests can help players discover these parts of the game, and have rewards to provide helpful shortcuts.     
Complete all quests of a special interest to complete its **Patron Quest** for very special rewards and incredible banners.        
But beware - some quests are very difficult!     
<img width="100" height="200" src="https://user-images.githubusercontent.com/55819817/174106133-c4250e0d-6c95-403d-a72d-8914826febd1.png">
![image](https://user-images.githubusercontent.com/55819817/174103070-8567ceac-f9b1-4624-8ae3-543187227804.png)

### Information
 
<img width="380" height="400" src="https://user-images.githubusercontent.com/55819817/174103926-52a741ac-6d36-44e4-8153-be5fb7aff6c1.png"><img width="380" height="400" src="https://user-images.githubusercontent.com/55819817/174105386-7985c35c-fc25-4d8b-bb5a-724d55a7ebf7.png">     
Quests are also home to information about the pack itself, as a helpful reference guide.   
**Introduction** quests cover's the pack's main features, while **Discrepancies** quests helps players know what isn't vanilla.

## Homebrew Changes

Yeah yeah, we get it - packs that just throw mods together are no fun. Here's what we pulled together besides our curation skills:

 - Four mods: 
   - [Portable Crafting Standalone](https://modrinth.com/mod/portable-crafting-standalone) - Press V or click a tab to use the crafting table in your inventory. 
   - [Totem Anywhere Standalone](https://modrinth.com/mod/totem-anywhere-standalone) - Totem of undying convenience - uses totems from inventory.  
   - [Crunchy Crunchy Advancements](https://modrinth.com/mod/crunchy-crunchy-advancements) - Hides and removes advancements - quests and [EMI](https://modrinth.com/mod/emi) covers all you need.
   - [Tinkerer's Smithing](https://modrinth.com/mod/tinkerers-smithing) - Repair for no XP cost, lower repair cost with scrap, and upgrade tool materials.
     - Flattens mending power creep, encouraging players to keep "Sentimental" tools as much as they like.
     - Tool material upgrades cost the exact same as a fresh tool - but keep the enchantments.
     - Quicker tools with less waste - upgrade wood to stone to iron from the 2x2 crafting grid.
  - Six data packs: (use [this](https://download-directory.github.io) for downloads)
   - [Tinkerer's Statures](https://github.com/sisby-folk/mc-packs/tree/quilt_1.18.2/config/openloader/data/tinkerers_statures) (Origins) - allows choosing player height on spawn.
   - [Tinkerer's Vegetarian](https://github.com/sisby-folk/mc-packs/tree/quilt_1.18.2/config/openloader/data/tinkerers_vegetarian) (NBT) - recipes for potions, leather, books, and more, without killing passive mobs.
   - [Tinkerer's Copper Beacons](https://github.com/sisby-folk/mc-packs/tree/quilt_1.18.2/config/openloader/data/tinkerers_copper_beacons) - Allows beacons made of unexposed copper blocks. A use for Copper and Wax!
   - [Tinkerer's Human't](https://github.com/sisby-folk/mc-packs/tree/quilt_1.18.2/config/openloader/data/tinkerers_humant) (Origins) - Removes mention of "human" and "nitwit" from origins/+classes descriptions.
   - Tinkerer's [Vampire](https://github.com/sisby-folk/mc-packs/tree/quilt_1.18.2/config/openloader/data/tinkerers_vampire)/[Imp](https://github.com/sisby-folk/mc-packs/tree/quilt_1.18.2/config/openloader/data/tinkerers_imp)/[Dryad](https://github.com/sisby-folk/mc-packs/tree/quilt_1.18.2/config/openloader/data/tinkerers_dryad) (Origins) - Mods of others' origins. Some small, some not - more planned.
 - Mod Configuration:
   - 194 Quests over 6 categories in Base (FTB Quests)
     - Just as many flavour text subtitles - queer humour, observations, and a weird mix of references.
     - An unholy amount of quest descriptions - how to achieve the task, what the required items do, etc.
     - Meticulously symmetrical and categorized quest positioning. No really. Hours and hours of it.
   - An uncomfortable amount of configuring mods avoid functionality overlap with other mods. Full days of it.
   - Thinking too hard about choosing keybinds that are easy to remember (We wish modifier keys were vanilla). 
 - Actually, a lot of just _thinking_. An intense amount. Mod suitability, configs, overlaps, bugs - we're _tired_.
   - This is still an endorsement, we swear.
   - There was a lot of notepad documents and messy organisation systems to get this done. We wrote a whole skyrim-style "modding guide" in early 2021 for what would eventually become this pack. Terrifying stuff.
   - Also reporting a lot of bugs and incompatibilities to mod developers. And quilt developers.
     - That's an endorsement too.
     - Thanks everyone.

## Features from Mods

All present minecraft modding is built on a decade of work from other people (and non-people, we don't discriminate).   
The rest of the cool stuff is just us bringing together the work of great modders in the community.    
Shoutouts are well-deserved here, so we're dropping links for all these major features. 

### Player Expression

Letting players express themselves with player customisation, builds, and even things like farming, cooking, and brewing, is a core tenet of the pack.
    
 - [Ears](https://ears.unascribed.com/) - Improved skins with support for tails, horns, ears, claws, wings and more species/gender things!
 - [Fabric Tailor](https://modrinth.com/mod/fabrictailor) - Swap your skin in-game. Perfect for plural systems.
 - [Origins](https://modrinth.com/mod/origins) - Choose a player _Origin_, granting abilities, limitations, and maybe species euphoria (we don't know you)
   - Uses our own curated set of custom and vanilla origins, with a separate selector for player height ("Stature")     

     <img width="700" height="262" src="https://user-images.githubusercontent.com/55819817/174215100-2b630688-8ef5-4429-b82e-9516c132915a.png">

 - [Drogtor](https://github.com/unascribed/Drogtor) - Change your player name at any time with a command!
 - [Player Pronouns](https://modrinth.com/mod/player-pronouns) - Set your pronouns in multiplayer and have them appear in chat.
 - [Fabrication](https://modrinth.com/mod/fabrication) - A huge tweak mod. Includes allowing players to hide armor to show their skin with a command.
 - [Presence Footsteps](https://modrinth.com/mod/presence-footsteps) - Footstep audio redone - allows swapping between bi/quadrupedal, with winged options.


 - [Carpet](https://github.com/gnembon/fabric-carpet) - A collection of tweaks. Here - it includes more dispenser functionality, for mechanics!
 - [Fabrication](https://modrinth.com/mod/fabrication) - Many minor tweaks to improve minecarts and train systems - for transit lovers.

## Usability and Accessibility

 - [EMI](https://modrinth.com/mod/emi) - An advanced recipe book that lets players find information on any item, and help craft it.
 - [What The Hell Is That?](https://modrinth.com/mod/wthit) - Hold alt to see information on the block or mob you're looking at.     
   ![image](https://user-images.githubusercontent.com/55819817/174112665-b8b534e2-5b8d-450e-91dd-260869086719.png)
 - [Notes](https://www.curseforge.com/minecraft/mc-mods/notes-fabric) - Allows players to take in-game notes about their plans, locations to revisit, etc.
 - [Reacharound](https://modrinth.com/mod/reacharound) - Build midair bridges without sneaking, and even downwards stairs.
 - [Project: Save The Pets!](https://modrinth.com/mod/projectsavethepets) - Prevents pet harm and adds a pet revival system.
 - [Horse Buff](https://modrinth.com/mod/horsebuff) - Improves and protects horses, making them easier to take out on adventures.
 - [Fabrication](https://modrinth.com/mod/fabrication) - A multitude of minor improvements, such as automatic block pickup and crawling.
 - [You're In Grave Danger](https://modrinth.com/mod/yigd) - Leaves a grave on death with your items and XP that won't de-spawn.

## Visuals

 - [Sodium](https://modrinth.com/mod/sodium) - Present day holy grail of performance mods.
 - [Iris](https://modrinth.com/mod/iris) - Optifine-compatible shaders. We recommend [Complementary](https://www.curseforge.com/minecraft/customization/complementary-shaders) or [Super Duper Vanilla](https://www.curseforge.com/minecraft/customization/super-duper-vanilla-shaders/files/).
 - Many more! Feel free to check the modlist.

---

# Known Issues

 - [Smithing/Vegetarian recipes aren't in EMI](https://github.com/Siphalor/nbt-crafting/issues/114)
 - [Petting mobs stops working randomly](https://github.com/Ellivers/Pettable/issues/4)
 - [Glow lichen says "Harvestable"](https://gitlab.com/ENDERZOMBI102/wthit-plugins/-/issues/5)
 - [Fogbox doesn't box fog](https://github.com/LudoCrypt/Fogbox/issues/6)
 - [EMI can't be accessed from quests](https://github.com/FTBTeam/FTB-Mods-Issues/issues/312)

---

# Modlist


```
Mods:
    AdvancementInfo
    Advancements Debug
    [Plus] Aileron
    Ambient Environment
    [Plus] Amplified Nether
    Animatica
    AppleSkin
    [Plus] Architecture Extensions
    Architectury API
    bad packets
    Balm (Fabric Edition)
    Better Biome Blend
    Better End Sky
    [Plus] Bits And Chisels
    [Modded] Botania
    [Plus] Campanion
    Cardinal Ice Boats
    Carpet Extra
    Carpet-Fixes
    Carpet
    [Plus] Chalk (Fabric)
    Charmonium
    CIT Resewn
    CleanCut
    Client Tweaks (Fabric Edition)
    Cloth Config API
    Consistency+
    Continuity
    Couplings
    Coyote Time
    [Modded] Create Fabric
    [Modded] CreatePlus
    Crowmap
    Crunchy Crunchy Advancements
    Cull Less Leaves
    [Plus] Dawn API
    Drogtor
    Dyeable Fishing Lines
    Dynamic FPS
    Dynamic View[Fabric]
    Ears (+ Snouts/Muzzles, Tails, Horns, Wings, and More)
    [Plus] Earth2Java
    Enhanced Block Entities
    Effective 💦
    EMI
    Enhanced Attack Indicator
    EntityCulling
    Extended Clouds
    [Plus] Fabric Seasons
    Fabrication
    Fabric Shield Lib
    Fabric Tailor
    Falling Leaves
    [Plus] Farmer's Delight [Fabric]
    Farsight [Fabric]
    FastOpenLinksAndFolders
    FerriteCore
    kennytvs-epic-force-close-loading-screen-mod-for-fabric
    ForgetMeChunk
    FTB Library (Fabric)
    FTB Quests (Fabric)
    FTB Teams (Fabric)
    [Plus] Fabric Waystones
    Grounded Origins
    [Plus] Halfdoors
    Horse Buff
    Hwyla Addon Horse Info
    Idwtialsimmoedm
    Illuminations 🔥
    Indium
    Iris Shaders
    Item Filters
    Item Model Fix
    JamLib
    Keep My Hand
    [Plus] Kiln
    Kiwi 🥝 (Fabric)
    Krypton
    LambdaBetterGrass
    LazyDFU
    Leaves Us In Peace
    Lithium
    [Plus] Lovely Snails
    LAN World Plug-n-Play (mcwifipnp)
    Loading Screen Tips
    [Plus] Meal API
    Memory Leak Fix
    Mod Settings for Fabric
    More Culling
    Mouse Wheelie
    [Plus] Nature's Compass
    Nbt Crafting (Fabric)
    NoRecipeBook (Fabric)
    Not Enough Animations
    Notes Fabric
    Ok Zoomer
    Open Loader
    Origins: Classes
    Origins
    [Plus] Overweight Farming
    [Modded] Patchouli
    Pehkui
    Pettable
    Player Pronouns
    [Plus] Polaroid Camera
    Portable Crafting Standalone
    Presence Footsteps
    Project: Save the Pets!
    [Plus] Promenade
    Puzzle
    Quilt Standard Libraries
    Quilt Loading Screen
    Raised
    Reacharound
    Reese's Sodium Options
    Reroll
    RightClickHarvest
    [Plus] Rusted Iron
    [Plus] Sandwichable
    Simple Fog Control
    Smooth Boot (Fabric)
    Snow! Real Magic! ⛄ (Fabric)
    Sodium Extra
    Sodium
    Starlight (Fabric)
    Status Effect Timer
    Styled Chat
    Styled Player List
    Tax Free Levels
    [Plus] TerraBlender (Fabric)
    [Plus] This Rocks!
    TieFix
    Tinkerer's Smithing
    ToolTipFix
    Totem Anywhere Standalone
    [Plus] Traveler's Titles (Fabric)
    [Plus] Trinkets
    True Darkness
    [Plus] Universal Ores
    VehicleFix
    Visuality
    WTHIT Plugins
    WTHIT
    You're in Grave Danger
    Your Options Shall Be Respected (YOSBR)
    [Plus] YUNG's API (Fabric)
    [Plus] YUNG's Better Desert Temples (Fabric)
    [Plus] YUNG's Better Dungeons (Fabric)
    [Plus] YUNG's Better Mineshafts (Fabric)
    [Plus] YUNG's Better Strongholds (Fabric)
    [Plus] YUNG's Better Witch Huts (Fabric)
    [Plus] YUNG's Extras (Fabric)

Jar mods:
    [Plus] Antique Atlas 6.2.0 1.18.2 (Unreleased)
    [Plus] Auroras Decorations 1.0.0 1.18 (Unreleased)
    Blanket Client tweaks 1.0.4
    colormatic 3.1.2-snapshot 1.18.2.jar (Create Compat)
    extraorigins 1.18-11 (temp due to quilt compat, license issues)
    fogbox 1.2.0
    inspecio 1.4.2 (Show repair cost)
    inventorytabs 0.6.1-1.18.x
    LambDynamicLights 2.1.1limitless1.18
    NoFade (1.18.2)
    Realistic Fishing (1.18.2)
    [Modded] Tinker's Construct 1.18.2 3.5.1 DEV.3d91fea0f (Unreleased)

Resource Packs: 
    Colored Axolotl Buckets With Babies
    Varied Connected Bookshelves
    xali's Enchanted Books
    Vanilla Tweaks
    [Plus] Nullscapes 1.18.2

Shader Packs Available:
    BSL Shaders
    Complementary Shaders
    Prismarine Shaders
    Sildurs Enhanced Default Shaders
    Super Duper Vanilla Shaders

Data Packs:
    Vanilla Tweaks
    (Origins) Lepus
    (Origins) OriginsPlus

Homebrew Data Packs:
    (Origins) Tinkerer's Statures
    (Origins) Tinkerer's Cleanup
    (Origins) Tinkerer's Human't
    (Origins) Vampire (ChessLord), Dryad (LuaDotExe), Imp (ExtaOrigins)
    Tinkerer's Vegetarian
    Tinkerer's Copper Beacons
```

# Special Thanks

Emi ([EMI](https://modrinth.com/mod/emi))     
Una ([Fabrication](https://github.com/unascribed/Fabrication), [Ears](https://modrinth.com/mod/ears), [Drogtor the Nickinator](https://github.com/unascribed/Drogtor/))     
QuiltComm and unascribed's Guild Discords      
Beta-testing Queer Pluralfolk       
[Bleu](https://twitter.com/bleudrawsthings) (for drawing the Kapesi headshot used in the icon)

# Credits 
```
Vanilla Tweaks: https://vanillatweaks.net/
OriginsPlus and Lepus: Dan's Other Clone https://www.youtube.com/c/DansOtherClone
Effective: https://www.curseforge.com/minecraft/mc-mods/effective     
Illuminations: https://www.curseforge.com/minecraft/mc-mods/illuminations     
```

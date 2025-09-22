# Proposed Ideas
## <u><i>NOTE: Ideas ทั้งหมดอาจมีการเปลี่ยนแปลงตามความยากง่ายของการทำ และเวลาที่เหลือในการทำ</i></u>
## Proposed Names
- [Add here]

## Docs
- https://docs.google.com/document/d/1u1e4y8OHD7AM01kfzar3d4c-t54qUJg0uEwbkN6Fz34/edit?tab=t.0
## Main Theme: <u>Rogue-Like / Turn-Based Dungeon Crawler</u>
### Objective Goal
- ลงดันเจี้ยนเป็๋นชั้นๆลึกลงไปเรื่อยๆ, เป้าหมายคือไปให้ลึกที่สุด เก็บ High Score เป็นความลึกที่ลงได้มากที่สุดก่อนจบเกม

### Main Game Machenics
- **Rogue-Like**
	- เริ่มเกมด้วยค่า HP(Health Point) หนึ่งๆ
	- หากตาย หรือแพ้ เกมจะเริ่มใมห่ตั้งแต่ต้นไม่มีจุดเซฟ
		- (อาจมีระบบเซฟก่อนออกเกมเพื่อโหลดกลับมาเล่นเมื่อเปิดเกมครั้งถัดไป)
- **Turn-Based**
	- ระบบเกมจะเริ่มที่ผู้เล่นเป็นคนเริ่ม turn และวนไปเลื่อยๆ
	- เลือกได้ว่าจะใช้ action หรือ escape (เสียครึ่งหนึ่งของ HP เพื่อหนี [escape penalty])

### Map / Floors / Rooms
- Map ของแต่ละชั้น(floor) อาจมีห้อง(room)หลายๆ ห้องติดกันอยู่ ในแต่ละห้อง(room)มีโอกาศที่จะมีบรรไดไปชั้น(floor)ต่อไปอยู่ตาม 1/Rn โดยที่ Rn เป็นจำนวนห้องทั้งหมดที่อยู่บนชั้น(floor)นั้น
- ในแต่ละห้องมี**อย่างน้อง** 1 loot chest ที่มีโอกาศดรอปของ .g. อาวุธ(weapons), consumable, single-use items, etc ตาม rarity
- ทุกๆ N ชั้น จะได้พักเติมของ เพิ่มความเก่ง ETC
- นอกจากทุก N ชั้นจะมีจุดพักให้เติมเลือด อาจมีโอกาศ 1/10 หรือ 1/25 ชั้น ที่ชั้นนั้นจะเป็น Black market หรือจุดพัก etc **(เพิ่มความคาดเดายากของเกม)**
- เจอและสู้มอนสเตอร์ในแต่ละชั้น(floor) / ห้อง(room) และดรอปของ e.g. อาวุธ(weapons), consumable, single-use items, etc ตาม rarity
- ในทุก N ชั้นจะมีห้องบอสอยู่

### In-game Events
- ในแต่ละชั้นอาจมี encounter/random events เกิดขึ้น
	- ในแต่ละการกระทำ(action)จะมีอัตราความสำเร็จ
	- ในแต่ละ encounter/event ตัวเลือกของผู้เล่นจะส่งผลต่อเหตุการณ์ต่อๆ ไปในเกม

## Proposed Engine
- **RPG Maker MV/MZ** (No direct Python integration) (JavaScript heavy, Python to manipulate files/saves externally) (Premade turn-based framework, significant time saved)
- **Pygame** (Native Python) (Build from scratch, full system control, most time consuming)
- **Unity** (with plugins - Python for Unity, IronPytohn) (C# heavy logic)
- **Godot** (with GDscript similair to Python)

## Engine Notes
### RPG Maker MV/MZ
- Easiest for time constraints (already has battle system, inventory, events).
- Downside: Limited flexibility, but enough for a dungeon-crawler.

### Pygame
- Gives max freedom but eats most time → risky for a final project unless the team is very experienced.

### Unity
- Strong choice if team is okay with C#. Many existing roguelike frameworks to borrow ideas from.

### Godot
- Good balance (GDScript is Python-like, rapid prototyping possible).
- Strong 2D support, easier than Unity for this scope.

### Members
- 68070003 กฤตภาส ไพรสาลี
- 68070035 ฐิติวัฒน์ มนต์วิเศษ
- 68070083 นัธทวัฒน์ พละเดช
- 68070150 เมธา ภัทรพิชญกุล

### Program
- <a href="https://godotengine.org">Godot</a>
### Related Topics
- <a href="https://forums.rpgmakerweb.com/index.php?threads/tips-for-a-dungeon-crawler.91343" target="_blank">Tips for Dungoen Crawler</a>
- <a href="https://www.youtube.com/watch?v=5HR4rQ52T2k" target="_blank">7 Levels of Indie Games</a>
- <a href="https://www.youtube.com/watch?v=JjxH0IuyCpg" target="_blank">Minecraft Is Not A Game(Minecraft and the philosophy of games)</a>

# 🐍 Snake Survive – Game Design Document

## 🎮 Core Concept
Snake Survive is a modern twist on the classic snake game for Android & iOS.  
Instead of moving on a grid, the snake moves freely across the map. The goal is survival against waves of enemies, using fruits to grow longer and mounting weapons on the snake’s back to fight off enemies.

---

## ⚙️ Core Gameplay Loop
1. **Start** → Player controls a snake, eats fruit to grow.  
2. **Progression** → Enemies begin spawning after the first fruit.  
3. **Combat** → Snake avoids enemies while mounted guns auto-fire.  
4. **Survival** → Player balances growth, weapon choice, and stamina.  
5. **End States** →  
   - Lose: Snake HP reaches 0.  
   - Win: Based on game mode (10 min, 5 min, or endless).  
6. **Replay** → Earn coins, unlock skins, and climb leaderboards.

---

## 🐍 Snake & Weapons
- Weapons **do not replace body segments**.  
- They **mount on the snake’s back** at available slots.  
- Number of slots depends on snake length (e.g., 1 gun every 2–3 segments).  
- If no slots are free, the player cannot pick up new weapons unless they:  
  - **Drop last weapon** (button), which spawns it back on the map for swapping.  

### 🔫 Weapons
- **Basic Turret** → standard bullets.  
- **Spread Blaster** → cone of projectiles.  
- **Laser Beam** → piercing shot.  
- **Missile Launcher** → splash damage.  
- **Flamethrower** → short-range fire.  
- **Utility Guns** → Freeze Ray (slow), Shield Projector (temporary shield).  

Each weapon has unique firing behavior and rate. Visualized directly on the snake’s body.

---

## 👾 Enemies
Enemies spawn after first fruit, scaling over time.  

1. **Basic Chaser** – standard pursuer.  
2. **Fast Runner** – weak but quick.  
3. **Tank** – slow, high HP.  
4. **Shooter** – ranged attacks.  
5. **Swarmers** – spawn in packs.  
6. **Elite/Boss** – rare, special abilities (dash, poison trail, shield).  

---

## 🎯 Game Modes
1. **Normal Mode**  
   - Survive 10 minutes.  
   - Balanced pacing.  
   - Medium rewards.  

2. **Quick Game**  
   - 5 minutes.  
   - Faster enemy scaling.  
   - Smaller rewards.  

3. **Extreme Mode**  
   - Endless survival.  
   - No map shrinking.  
   - Enemies scale infinitely.  
   - High rewards + leaderboard focus.  

---

## ⚡ Snake Abilities
- **Boost Button** → short speed burst.  
  - Costs **stamina only**.  
  - Stamina regenerates slowly.  
  - Encourages strategic use for dodging ambushes.  

---

## 🏆 Win & Lose Conditions
- **Lose:** Snake HP = 0 → Game Over.  
- **Win:**  
  - Normal → survive 10 min.  
  - Quick → survive 5 min.  
  - Extreme → endless leaderboard.  

Rewards scale by performance: time, kills, score.  

---

## 🔄 Meta Progression
- Earn **coins** each run.  
- Spend on:  
  - Snake skins.  
  - Weapon skins.  
  - Visual effects (snake trails, muzzle flashes).  
- Daily/weekly challenges to keep engagement high.  

---

## 📱 Mobile Controls & UI

### HUD
- **Top Bar** → Score (center), HP (left), Stamina (right).  
- **Bottom Left** → Virtual joystick (movement).  
- **Bottom Right** → Boost button + Drop Gun button.  
- **Right Side** → Weapon slots (shows mounted guns).  

### Menus
- **Main Menu:** Play, Shop, Leaderboard, Settings, Daily Challenge.  
- **Game Mode Select:** Choose Normal, Quick, or Extreme before run.  
- **Game Over:** Show time survived, kills, score, coins, with Retry/Main Menu/Share Score buttons.

---

## 🔄 Gameplay Flow (Summary)
**Eat → Grow → Mount Weapons → Fight Enemies → Survive → Earn Rewards → Upgrade → Replay.**


// Printo "Hello, World!"
console.log("Hello, World!");

// Kërko emrin e përdoruesit
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Si quhesh? ", (emri) => {
    console.log(`Përshëndetje, ${emri}!`);

    // Printo datën dhe orën aktuale
    const tani = new Date();
    console.log(`Data dhe ora aktuale: ${tani}`);

    rl.close();
});

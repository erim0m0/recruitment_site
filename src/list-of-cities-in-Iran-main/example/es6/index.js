import { readFile } from "fs/promises";

const cities = JSON.parse(
  await readFile(new URL("../../json/cities.txt", import.meta.url))
);

const provinces = JSON.parse(
  await readFile(new URL("../../json/provinces.json", import.meta.url))
);

console.log("---------", cities);
console.log("<br>", "---------", provinces);

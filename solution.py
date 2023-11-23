function serialize(nums) {
  return nums.join(',');
}

function deserialize(str) {
  return str.split(',').map(Number);
}

//TC
const tests = [
  [1, 2, 3],            // Short test
  Array.from({length: 50}, () => Math.floor(Math.random() * 300) + 1),  // Random - 50 numbers
  Array.from({length: 100}, () => Math.floor(Math.random() * 300) + 1), // Random - 100 numbers
  Array.from({length: 500}, () => Math.floor(Math.random() * 300) + 1), // Random - 500 numbers
  Array.from({length: 1000}, () => Math.floor(Math.random() * 300) + 1), // Random - 1000 numbers
  Array.from({length: 10}, (_, index) => index + 1), // Boundary - all numbers of 1 digit
  Array.from({length: 90}, (_, index) => index + 10), // Boundary - all numbers of 2 digits
  Array.from({length: 200}, (_, index) => index + 100), // Boundary - all numbers of 3 digits
  Array.from({length: 900}, (_, index) => (index % 300) + 1) // 3 of each number - 900 numbers in total
];

tests.forEach((test, index) => {
  const originalString = JSON.stringify(test);
  const compressedString = serialize(test);
  const compressionRatio = (compressedString.length / originalString.length) * 100;

  console.log(`Test ${index + 1}:`);
  console.log(`Original: ${originalString}`);
  console.log(`Compressed: ${compressedString}`);
  console.log(`Compression Ratio: ${compressionRatio.toFixed(2)}%\n`);
});

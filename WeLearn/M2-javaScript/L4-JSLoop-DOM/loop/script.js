const names = ['Alice', 'Bob', 'Charlie', 'Deborah', 'Evan'];
for (let i = 0; i < 5; i++) {
  console.log(names[i]);
}
names.forEach((name) => {
  //run this function for each name in names
  console.log(name);
})

let numbers=[1,2,3,4,5,6,7,8,9,10];
const findTotal =((item) => {
  let total = 0
  for (let i = 0; i < 10; i++){
    total += item[i];
    console.log("total")
  }
  console.log('Total: ' + total);
});

const buttons = document.querySelectorAll('button');
const box = document.querySelectorAll('#box')

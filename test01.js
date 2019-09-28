var colors = ['yellow', 'royalblue', 'rosybrown', 'powderblue', 'sienna', 'gray'];
var length = colors.length;
var num = 0;

function insert() {
  let color = colors[num % length];
  num++;
  const container = document.querySelector('#container');
  const box = document.createElement('div');
  box.classList.add('box');
  box.style.background = color;
  container.appendChild(box);
}

function pop() {
  let boxes = document.querySelectorAll('.box');
  let length = boxes.length;
  if (length > 0) {
    boxes[length - 1].remove();
    num--;
  }

}
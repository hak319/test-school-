const reviewList = [
    {
        id: 1,
        name: "steak",
        type: "indoor",
        img: "bike3.jpg",
        text: "pro"
    },
    {
        id: 2,
        name: "steak",
        type: "indoor",
        img: "bike2.jpg",
        text: "pro"
    },
    {
        id: 3,
        name: "steak",
        type: "indoor",
        img: "bike.jpg",
        text: "pro"
    }
]

const mainImg = document.querySelector("#main-img");
const foodName = document.querySelector("#food-name");
const type = document.querySelector("#type")
const info = document.querySelector("#info")

const preBtn = document.querySelector("#prev-btn");
const nextBtn = document.querySelector("#next-btn");

let currentIndex = 1;

window.addEventListener("DOMcontentLoaded", function(){
    let iteam = reviewList[currentIndex];
    mainImg.src = iteam.img;
    foodName.textContent = iteam.name;
    type.textContent = iteam.type;
    info.textContent = iteam.text;
})
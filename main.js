const menuInfo = document.querySelector(".info");
const menuPortfolio = document.querySelector(".portfolio");

function showInfo(){
menuPortfolio.classList.toggle("hide");
}
function showPortfolio(){
menuInfo.classList.toggle("hide");
}

const menuBtn = document.querySelector(".menu__btn");
const menuList = document.querySelector(".menu__list");
function toggleMenuVisibility() {
menuList.classList.toggle("hide");
}
menuBtn.addEventListener("click", toggleMenuVisibility);

const menuPtf = document.querySelector(".portfolio__btn");
const menuP = document.querySelector(".menu__portfolio");
function togglePortfolioVisibility() {
menuP.classList.toggle("hide");
}
menuPtf.addEventListener("click", togglePortfolioVisibility);

const menuLab1 = document.querySelector(".lab1__btn");
const menuL1 = document.querySelector(".lab_1");
function toggleFirstVisibility() {
menuL1.classList.toggle("hide");
}
menuLab1.addEventListener("click", toggleFirstVisibility);

const menuLab2 = document.querySelector(".lab2__btn");
const menuL2 = document.querySelector(".lab_2");
function toggleSecondVisibility() {
menuL2.classList.toggle("hide");
}
menuLab2.addEventListener("click", toggleSecondVisibility);
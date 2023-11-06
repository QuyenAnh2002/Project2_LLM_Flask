const popup = document.querySelector('.chat-popup');
const chatBtn = document.querySelector('.back-to-top');
// const submitBtn = document.querySelector('.submit');
const chatArea = document.querySelector('.chat-area');
// const inputElm = document.querySelector('input');
// const emojiBtn = document.querySelector('#emoji-btn');
const picker = new EmojiButton();

chatBtn.addEventListener('click', ()=>{
    popup.classList.toggle('show');
})

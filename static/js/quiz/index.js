// show meaning when click quiz-header
const meaning = document.querySelector("#meaning");

const quiz_header = document.getElementById("quiz-header");
quiz_header.addEventListener("click", function () {
  meaning.classList.toggle("hidden");
});

// Press arrow right
document.addEventListener("keydown", (e) => {
  const key = e.key;

  switch (key) {
    case "ArrowRight":
      window.location.href = "";
      return;
  }
});

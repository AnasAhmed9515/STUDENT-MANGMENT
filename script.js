document.addEventListener("DOMContentLoaded", function () {

    // Smooth scrolling
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(function (link) {

        link.addEventListener("click", function (event) {

            const targetId = this.getAttribute("href");

            const target = document.querySelector(targetId);

            if (target) {

                event.preventDefault();

                target.scrollIntoView({
                    behavior: "smooth"
                });

            }

        });

    });


    // Automatically hide messages
    const messages = document.querySelectorAll(".message");

    messages.forEach(function (message) {

        setTimeout(function () {

            message.style.opacity = "0";

            message.style.transition = "opacity 0.5s";

            setTimeout(function () {

                message.remove();

            }, 500);

        }, 4000);

    });


    // Prevent marks above 100
    const markInputs =
        document.querySelectorAll('input[type="number"]');

    markInputs.forEach(function (input) {

        input.addEventListener("input", function () {

            if (this.value > 100) {
                this.value = 100;
            }

            if (this.value < 0) {
                this.value = 0;
            }

        });

    });

});
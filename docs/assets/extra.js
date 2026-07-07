/* In the mobile drawer, tapping a section row expands it instead of
   navigating to the section's index page (see extra.css). To keep those
   index pages reachable, prepend an "Overview" link inside each section's
   subnav. Hidden on desktop, where the section label itself is the link. */
document.addEventListener("DOMContentLoaded", function () {
  document
    .querySelectorAll(".md-nav__item--section > .md-nav__container > a.md-nav__link")
    .forEach(function (anchor) {
      var item = anchor.closest(".md-nav__item");
      var list = item && item.querySelector(":scope > nav > ul.md-nav__list");
      if (!list) return;
      var li = document.createElement("li");
      li.className = "md-nav__item ss-index-item";
      var link = document.createElement("a");
      link.className = "md-nav__link";
      link.href = anchor.href;
      link.textContent = "Overview";
      li.appendChild(link);
      list.insertBefore(li, list.firstChild);
    });
});

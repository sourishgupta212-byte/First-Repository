
const workspace = document.getElementById("workspace");
const buttons = document.querySelectorAll("[data-view]");
const views = {
    pending: `
        <h2>Pending Applications</h2>
        <p>Applications awaiting processing.</p>
    `,
    "under-review": `
        <h2>Under Review</h2>
        <p>Applications currently being processed.</p>
    `,
    ready: `
        <h2>Ready for Decision</h2>
        <p>Applications awaiting your final decision.</p>
    `,
    send: `
        <h2>Send Requests</h2>
        <p>Prepare correspondence for other ministries.</p>
    `,
    mailbox: `
        <h2>Mailbox</h2>
        <p>Your incoming correspondence will appear here.</p>  `
};
buttons.forEach(function(button) {
    button.addEventListener("click", function() {
        const view = button.dataset.view;
        workspace.innerHTML = views[view];
    });
});

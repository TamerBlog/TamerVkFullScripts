const colors = require('colors');

console.log(`Initializing Vk-killer`.red.bold);
const { 
    TOKEN,
    CHAT_SPAM,
    GROUP_ID,
    BTN_TEXT,
    HELLO_TEXT,
    TIME
} = require("./72347283498629346288");

console.log(`Vk-killer>> Starting...`.blue.bold);

const { VK, Keyboard } = require("vk-io");
const vk = new VK({
    token: TOKEN,
    apiMode: "parallel",
    pollingGroupId: GROUP_ID,
    apiVersion: 5.101
});

vk.updates.use(async (ctx, next) => {
    if (ctx.is("message") && ctx.isOutbox) {
        return;
    }

    if (ctx.isChat) {
    	console.log(`Vk-killer bot >> New chat has been attacked..`.green.bold);
        setInterval(() => {
            ctx.send({
                message: randomFromArray(CHAT_SPAM),
                keyboard: Keyboard.keyboard(
                    Array(10).fill().map(() => 
                       Array(4).fill().map(() => button(randomFromArray(BTN_TEXT)))
                    )
                )
            });
        }, TIME);
    }

    return ctx.send(HELLO_TEXT);
});

vk.updates.startPolling()
    .then(() => console.log(`Vk-killer bot >> Started...`.yellow.bold,`\nЭто я: https://vk.com/tamerblogchatkiller`.green.bold));

const randomInt = (x, y) => y ? Math.round(Math.random() * (y - x)) + x : Math.round(Math.random() * x);
const randomFromArray = (array) => array[randomInt(array.length - 1)];
const button = (label) => {
    return Keyboard.textButton({
        label, color: Keyboard[randomFromArray(["POSITIVE_COLOR", "DEFAULT_COLOR", "PRIMARY_COLOR", "NEGATIVE_COLOR"])]
    });
}
process.on("uncaughtException", e => {
  console.log(e);
});

process.on("unhandledRejection", e => {
  console.log(e);
});

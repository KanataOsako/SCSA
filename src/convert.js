const slackifyMarkdown = require('slackify-markdown');

function convertMarkdownToSlack(markdownText) {
    return slackifyMarkdown(markdownText);
}

// 関数をエクスポート
module.exports = { convertMarkdownToSlack };

// 直接実行された場合の処理
if (require.main === module) {
    const inputText = process.argv[2];
    if (inputText) {
        console.log(convertMarkdownToSlack(inputText));
    } else {
        console.error('Error: No input text provided.');
        process.exit(1);
    }
}
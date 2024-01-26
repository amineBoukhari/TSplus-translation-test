import OpenAI from "openai";
import fs from "fs"

const key = fs.readFileSync('./key-gpt', 'utf8');

const openai = new OpenAI( {apiKey : key} );
const content = fs.readFileSync('./text.md', 'utf8');

let output="" ;

async function main() {
    const stream = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [{ role: "user", content: "translate this to french : " + content  }],
        stream: true,
    });
    for await (const chunk of stream) {
        process.stdout.write(chunk.choices[0]?.delta?.content || "");
        output+=chunk.choices[0];
    }

    console.log("translte's done\n")
    console.log(output)
}

main();
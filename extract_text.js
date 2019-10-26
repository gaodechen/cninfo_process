var fs = require('fs')
var extract = require('pdf-text-extract')

var input = process.argv.slice(2)[0]
var output = process.argv.slice(2)[1]

extract(input, function (err, pages) {
    if (err) {
        console.dir(err)
        return
    }
    fs.writeFile(output, pages, (error) => {
        if (error) {
            console.log(error);
        } else {
            console.log(output + " DONE")
        }
    });
})
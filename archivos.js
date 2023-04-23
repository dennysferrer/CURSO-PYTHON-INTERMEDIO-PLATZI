const fs = require('fs');


const read = () => {
    fs.readFile("./archivos/numbers.txt", "utf-8", (err, data) => {
        if(err){
            throw err;
        }

        console.log(data);
    });


}


const write = () => {
    const names = ["Dennys", "Maria", "Pedro", "Lucas", "Enrique"];
    names.forEach((name) => {
        fs.writeFileSync("./archivos/names2.txt", name, "utf-8");
        console.log(name);
    })
    
}

read();
write()


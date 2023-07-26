type heroi= {
    name: string;
    vulgo: string;
};
const pessoa: heroi;

function printaObjetos(pessoa: heroi){
    console.log ("pessoa: ", pessoa);
}

printaObjetos(`{
    name: "Bruce Wayne",
    vulgo: "Batman",
}`);

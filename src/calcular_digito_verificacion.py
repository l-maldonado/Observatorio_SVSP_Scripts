# Este Script sirve para verificar que un NIT está bien formateado al permitir asignar un código de verificación a un NIT de entrada

# este escript se puede extender para que además de retornar el código de verificación, entregue una interpretación del NIT de entrada,
# según las categorías: Persona natural, Negocio, etc.

# A futuro, si fuera posible, se podría extender la funcionalidad aún más, para que automáticamente haga una consulta a la API del RUES
# y retorne otros datos acerca del registro mercantíl en la cámara de Comercio de la empresa a la cual eprtenece dicho NIT.

# Este4 código está inspirado en el código publicado en https://github.com/druckern/GenerarDigitoVerificacion

'''
let nit = "79886653"; // Carry out the necessary validations on the captured number. CAPM.
const base = [3,7,13,17,19,23,29,37,41,43,47,53,59,67,71];
const DIVIDER = 11;
let checkDigit;
let accumulator = 0;

let reverseString = (str) => str.split("").reverse();


let arrayString = reverseString(nit);

for (let index = 0; index < arrayString.length; index++) {
    let calculation = Number(arrayString[index]) * base[index]; 
    accumulator += calculation;   
}
 
let calculationBasis = accumulator % DIVIDER;
checkDigit = calculationBasis > 1 ? DIVIDER - calculationBasis: calculationBasis;

console.log(checkDigit);

'''

def


if __name__ == '__main__':
    process_nit()

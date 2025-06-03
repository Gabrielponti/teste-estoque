const mascaraMoeda = (event) => {
  const onlyDigits = event.target.value.replace(/\D/g, "").padStart(3, "0");
  const digitsFloat = onlyDigits.slice(0, -2) + "." + onlyDigits.slice(-2);
  event.target.value = maskCurrency(digitsFloat);
};

const maskCurrency = (valor, locale = "pt-BR", currency = "BRL") => {
  return new Intl.NumberFormat(locale, { minimumFractionDigits: 2 }).format(
    valor
  );
};


class ValidadorCliente:
    def email_parece_valido(self, email):
        return (
            "@" in email
            and "." in email.split("@")[-1]
            and not email.startswith("@")
        )

    def validar(self, cliente):
        vazios = []

        if not cliente.nome.strip():
            vazios.append("Nome")

        if not cliente.telefone.strip():
            vazios.append("Telefone")

        if not cliente.email.strip():
            vazios.append("E-mail")

        if not cliente.endereco.strip():
            vazios.append("Endereço")

        if vazios:
            return f"Preencha o(s) campo(s): {', '.join(vazios)}"

        if not cliente.telefone.isdigit():
            return "Telefone inválido: use somente números."

        if not self.email_parece_valido(cliente.email):
            return "E-mail inválido."

        return None

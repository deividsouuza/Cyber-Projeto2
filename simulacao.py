def main():
    print("SIMULAÇÃO EDUCATIVA — sem captura, criptografia ou rede\n")

    sample_files = ["relatorio.txt", "foto.jpg"]
    print(f"[RANSOMWARE] arquivos fictícios: {', '.join(sample_files)}")
    print("[RANSOMWARE] estado simulado: acessíveis -> indisponíveis (apenas modelo)")
    print('[RANSOMWARE] nota fictícia: "Seus arquivos foram bloqueados." (não há resgate real)')

    synthetic_key_events = ["[tecla A]", "[tecla B]", "[ENTER]"]
    print(f"[KEYLOGGER] eventos sintéticos: {synthetic_key_events}")
    print("[KEYLOGGER] captura real: não realizada")
    print("[EXFILTRAÇÃO] envio de dados: bloqueado/não implementado\n")

    defenses = [
        "backups offline testados",
        "princípio do menor privilégio",
        "EDR/antivírus",
        "atualizações",
        "MFA",
        "conscientização",
    ]
    print("Defesas: " + ", ".join(defenses) + ".")


if __name__ == "__main__":
    main()
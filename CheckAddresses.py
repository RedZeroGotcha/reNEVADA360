# TODO write a description for this script
#@author
#@category _NEW_
#@keybinding
#@menupath
#@toolbar
#@runtime Jython

addresses_to_check = [
    "0x82E55E48",
]

fm = currentProgram.getFunctionManager()
addr_factory = currentProgram.getAddressFactory()

print("=" * 70)
print("Verificacao de enderecos nao resolvidos")
print("=" * 70)

for addr_str in addresses_to_check:
    clean = addr_str.replace("0x", "").replace("0X", "")
    addr = addr_factory.getAddress(clean)

    if addr is None:
        print(addr_str + " -> ENDERECO INVALIDO (fora do espaco de memoria do programa)")
        continue

    func_containing = fm.getFunctionContaining(addr)
    func_at = fm.getFunctionAt(addr)

    if func_at is not None:
        print(addr_str + " -> JA E o INICIO de uma funcao: " + func_at.getName() +
              " (inicio=" + str(func_at.getEntryPoint()) + ")")
    elif func_containing is not None:
        body = func_containing.getBody()
        print(addr_str + " -> Fica DENTRO da funcao: " + func_containing.getName() +
              " (inicio=" + str(func_containing.getEntryPoint()) +
              ", fim=" + str(body.getMaxAddress()) + ")")
        print("   >> Sugestao: declarar como CHUNK dessa funcao pai no manifest.")
    else:
        print(addr_str + " -> NAO pertence a nenhuma funcao conhecida pelo Ghidra")
        instr = getInstructionAt(addr)
        if instr is not None:
            print("   >> Tem instrucao valida ali: " + str(instr))
            print("   >> Sugestao: pode ser uma FUNCAO NOVA nao descoberta ainda.")
        else:
            data = getDataAt(addr)
            if data is not None:
                print("   >> E uma regiao de DADO, nao codigo: " + str(data))
            else:
                print("   >> Sem instrucao nem dado definido ali - regiao nao analisada.")

print("=" * 70)
print("Fim da verificacao.")

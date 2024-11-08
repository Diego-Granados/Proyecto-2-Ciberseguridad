section .text
global _start

_start:
    xor rax, rax          ; 0 en rax
    push rax              ; terminar el string con 0
    mov rdi, "/bin//sh" ;
    push rdi              ; Poner el string en la pila
    mov rdi, rsp          ; Mover el puntero a "/bin//sh" a rdi

    ; Construir argumento argv[]
    push rax              ; argv[1] = 0 (NULL)
    push rdi              ; argv[0] apunta a "/bin//sh"
    mov rsi, rsp          ; Mover el puntero de argv[] a rsi

    ; Variables de entorno
    xor rdx, rdx          ; No hay variables de entorno (envp = NULL)

    ; Invocar execve()
    mov al, 59           ; Codigo para System call execve es 59 en 64-bits
    syscall               ; Hacer el syscall


; /bin//sh = 0x2f62696e2f2f7368 
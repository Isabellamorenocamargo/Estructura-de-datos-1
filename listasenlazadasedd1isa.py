# -*- coding: utf-8 -*-
"""ListasEnlazadasEDD1isa.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GRRJ9jBo4nv4gSzbqnTpBzPhk9O57Xz8
"""

#BONUS EDD1 ISABELLA MORENO CAMARGO

class Nodo:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class Lista_enlazada:
    def __init__(self):
        self.head = None

    #Metodo para insertar dato (nodo) en una posicion x
    def insertar_en_posicionx_(self,posicion, dato):
        if posicion == 0:  # insertar en primera posicion
            nuevonode = Nodo(dato, self.head)
            self.head = nuevonode
            return

        anterior=None
        actual=self.head
        nuevonode= Nodo(dato) # crear nuevo nodo con el dato

        if actual is None: # si la lista esta vacia, agregar el nuevo nodo como head
            self.head = nuevonode
            return

        for i in range (posicion):
            if actual is None: # if position is greater than the length of the list, insert at the end
                anterior.next = nuevonode
                return
            anterior=actual
            actual=actual.next

        anterior.next = nuevonode  #referencia a posicion de neuvo
        nuevonode.next = actual #referente a posicion actual del nodo a rodar

      #Metodo para insertar nodo despues de referencia o key
    def insertar_nodo_despues_de_ref_(self,keyf, dato):

          anterior=None
          actual=self.head
          nuevonode=Nodo(dato)

          while actual and actual.data != keyf:
              anterior=actual
              actual=actual.next

          if actual is None: # al no encontrar la referencia, no ocurre nada
              return
          nuevonode.next=actual.next
          actual.next=nuevonode


  # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" --> ")
            node = node.next


Mi_lista = Lista_enlazada() # Instancia de la clase


Mi_lista.insertar_en_posicionx_(0, "a") #ingresar estos datos en la lista para despues probar metodo pidiendo datos
Mi_lista.insertar_en_posicionx_(1, "b")
Mi_lista.insertar_en_posicionx_(2, "c")
Mi_lista.insertar_en_posicionx_(3, "d")
Mi_lista.insertar_en_posicionx_(4, "e")

#leer datos para Metodo de insertar en posicion x
print("ingrese posicion en la que quiere insertar el dato no mayor a posicion 5")
posicion=int(input())
print("inserte dato a ingresar")
dato=input()

Mi_lista.insertar_en_posicionx_(posicion, dato)  #Metodo para insertar dato (nodo) en una posicion x   """

Mi_lista.print_list() # Imprimimos la lista de nodos

#leer datos para método de insertar despues de referencia
print("\n insertar referencia")
keyf=input()

print("inserte dato a ingresar")
dato=input()

Mi_lista.insertar_nodo_despues_de_ref_(keyf,dato)  #Metodo para insertar nodo despues de referencia o key
Mi_lista.print_list() # Imprimimos la lista de nodos
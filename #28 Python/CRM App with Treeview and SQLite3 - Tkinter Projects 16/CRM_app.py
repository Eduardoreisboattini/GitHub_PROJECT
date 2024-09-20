from tkinter import *
from tkinter import ttk
          
        root = Tk()
        root.title('Codemy.com - TreeBase')
        root.iconbitmap('c:/gui/codemy.ico')
        root.geometry("1000x500")
        
# Add Some Style
style = ttk.Style
# Pick a Theme
style.theme_use('default')
# configure the treeview colors
style.Configure("Treeview",
                background="#D3D3D3",
                foreground='black',
                rowheight=25,
                fieldbackground='#D3D3D3')
        # Change selected Color
        style.map('Treeview
                  bacground=[('selected','#347083)']
        # Create a TreeView Frame
        tree_frame = Frame(root) 
        tree_frame.pack(pady=10)
        
        # Create a TreeView scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)
        
        # Create the TreeView
        my_tree = ttk.TreeView(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        my_tree.pack()
        
        #Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)
        
         #Define Our Columnns
         my_tree['columns'] = (("Novo_GPS", "#Aliados", "Aliado_ID", "Nome_Aliado", "Genero", "Endereco", "Bairro", "Cidade", "Uf", "Pais", "Cep", "Latitude", "Longitude", "Email", "Data_Compra", "Origem", "Regiao", "Tipo_Regiao", "Micro_Região", "#GPS", "Realizado", "Dias_GPS")
        
        #Format Our Columnns
 my_tree.colum("#0","acnchor=W,width=140)
 my_tree.colum("Novo_GPS","acnchor=W,width=140)
 my_tree.colum("#Aliados","acnchor=W,width=140)
 my_tree.colum("Aliado_ID","acnchor=W,width=140)
 my_tree.colum("Nome_Aliado","acnchor=W,width=140)
 my_tree.colum("Genero","acnchor=W,width=140)
 my_tree.colum("Endereco","acnchor=W,width=140)
 my_tree.colum("Bairro","acnchor=W,width=140)
 my_tree.colum("Cidade","acnchor=W,width=140)
 my_tree.colum("Uf","acnchor=W,width=140)
 my_tree.colum("Pais","acnchor=W,width=140)
 my_tree.colum("Cep","acnchor=W,width=140)
 my_tree.colum("Latitude","acnchor=W,width=140)
 my_tree.colum("Longitude","acnchor=W,width=140)
 my_tree.colum("Email","acnchor=W,width=140)
 my_tree.colum("Data_Compra","acnchor=W,width=140)
 my_tree.colum("Origem","acnchor=W,width=140)
 my_tree.colum("Regiao","acnchor=W,width=140)
 my_tree.colum("Tipo_Regiao","acnchor=W,width=140)
 my_tree.colum("Micro_Região","acnchor=W,width=140)
 my_tree.colum("#GPS","acnchor=W,width=140)
 my_tree.colum("Realizado","acnchor=W,width=140)
 my_tree.colum("Dias_GPS","acnchor=W,width=140)
        
        # Add some columns to the TreeView
        
        # Add some rows to the TreeView
        
        # Bind the TreeView with a function to handle selection changes
        
        # Bind the TreeView with a function to handle double click events
        
        # Add some labels to the TreeView Frame
        
        # Add some entry fields to the TreeView Frame
        
        # Add some checkboxes to the TreeView Frame
        
        # Add some radio buttons to the TreeView Frame
        
        # Add some drop-down menus to the TreeView Frame
        
        # Add some text fields to the TreeView Frame
        
        # Add some scrollbars to the TreeView Frame
        
        # Add some buttons to the TreeView Frame
        
        # Add some labels to the TreeView Frame
        
        # Add some entry fields to the TreeView Frame
        
        # Add some checkboxes to the TreeView Frame
        
        # Add some radio buttons to the TreeView Frame
        
        # Add some drop-down menus to
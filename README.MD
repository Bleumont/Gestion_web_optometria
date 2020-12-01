---
# Sistema Web de gestión con Python y JavaScript
---

- Sistema implementado en Django.
- Estilos de Boostrap v4.5 y personalizados.
- Frontend responsivo hecho a mano con HTML, CSS y JS.
- Base de datos: SQLite.
- Demo de funcionamiento: [YouTube](https://www.example.com).
- GitHub: [Repo](https://github.com/Bleumont/Python_JS_PoloTic).

### El proyecto:

Sistema Web en Django que permite gestionar el diagnóstico de pacientes y la venta de productos Ópticos. Para ello cuenta con:

1. Un sistema con un login de usuario con los siguientes roles:

   - Secretaría
   - Profesional medico
   - Ventas
   - Taller
   - Gerencia

2. El rol de Secretaría permite agregar, modificar o eliminar los turnos de los Pacientes.

3. Cada Paciente tiene su historial médico (solo el Profesional médico puede agregar
   Observaciones al historial médico).

4. Cada Profesional médico puede ver el listado de Pacientes filtrando por día, mes o año.

   - El Profesional médico solo puede ver los Pacientes asignados a él mediante un Turno.

5. El rol de Ventas puede generar un pedido para el Paciente, donde detalla el Producto
   que quiere adquirir, el precio, la cantidad, un subtotal y el tipo de pago.

   - Si el producto está clasificado como Lente tendrá la opción de Lejos/Cerca, Izquierda/Derecha y si incluye Armazón o no.
   - Una vez que se genera el pedido queda en estado “Pendiente”.
   - Luego el rol de Ventas puede cambiar el estado a “Pedido” o mandarlo a “Taller”.

6. El rol de Taller solo visualiza la lista de pedidos enviados al Taller. También puede confirmar cambiando el estado del pedido a “Finalizado”.

7. Gerencia puede visualizar todos los datos sumados a los siguientes reportes:

   - Pacientes que asistieron a los turnos en la semana/mes.
   - Pacientes que no asistieron a los turnos en la semana/mes.
   - Pacientes que hicieron por lo menos un Pedido en la semana/mes.
   - Productos más vendidos en el mes.
   - Ventas totales por mes clasificadas por Vendedores.

---

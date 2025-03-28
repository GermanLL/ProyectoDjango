<template>
  <section class="py-5 text-center container" Style="background-image:url(assets/img/gallery/bg.png)">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h1 class="h1 fw-bold mb-0">Productos</h1>
        <p class="fs-1 mb-5">Sistema de gestión de pedidos optimizado. Mejora eficiencia y visibilidad. Más info
          en pedidos.</p>
      </div>
    </div>
    <div id="alerta" class="alert alert-success" role="alert">
      A simple success alert—check it out!
    </div>
    <div class="album py-5">
      <div class="container">
        <div class="card shadow-sm border-warning rounded-5 mb-3">
          <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
            <ul v-for="item in datosProducto" :key="item.id">
              <div class="card-body">
                <img :src="item.imagen" class="img-fluid" alt="..." width="400" height="341" />
                <h4 class="card-title">{{ item.nombre }}</h4>
                <p class="card-text">{{ item.descripcion }}</p>
                <p class="card-text">Precio: $ {{ item.precio }}</p>
                <span v-if="isLogged">
                  <span v-if="pedidoAbierto">
                    <button v-on:click="agregarAPedido(item.id)" class="btn btn-outline-danger" type="button">
                      Agregar a pedido </button>
                  </span>
                </span>
              </div>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

</template>

<script>
import axios from "axios";
export default {
  //////
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Producto",
  data() {
    return {
      datosProducto: {},
    };
  },
  ///////
  methods: {
    getProductos() {
      var alerta = document.getElementById("alerta");
      alerta.style.display = "none";
      axios({
        url: "http://127.0.0.1:8000/producto/",
        headers: {},
        method: "GET",
      }).then((response) => {
        this.datosProducto = response.data;
      });
    },
    agregarAPedido(idProducto) {
      axios({
        url: "http://127.0.0.1:8000/productopedido/agregar/",
        headers: { Authorization: "Token" + this.$store.getters.getToken },
        method: "POST",
        data: {
          idProd: idProducto,
          idPed: this.$store.getters.getIdPedidoAbierto,
        },
      });
      var alerta = document.getElementById("alerta");
      alerta.style.display = "block";
    },
  },
  mounted() {
    var alerta = document.getElementById("alerta");
    alerta.style.display = "none";
    this.getProductos();
  },
  computed: {
    isLogged() {
      return this.$store.getters.getIsLog;
    },
    pedidoAbierto() {
      return (this.$store.getters.getIdPedidoAbierto != 0);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

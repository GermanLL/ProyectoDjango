<template>
  <section class="py-5 text-center container" Style="background-image:url(assets/img/gallery/bg.png)">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h1 class="h1 fw-bold mb-0">Detalle pedido</h1>
        <p class="fs-1 mb-5">Sistema de gestión de pedidos optimizado. Mejora eficiencia y visibilidad.</p>
      </div>
    </div>
    <div class="container">
      <div class="row h-100 justify-content-center">
        <div class="col-md-6 col-lg-5 col-xl-4">
          <div class="card h-100 px-lg-5 card-span">
            <div class="card-body d-flex flex-column justify-content-around">
              <div class="text-center pt-5">
                <h2 class="display-3">Descripcion {{ this.$route.params.id }}</h2>
                <ul>
                  <div class="row">
                    <li v-for="item in datosPedido" :key="item">
                      <div class="col-12 col-sm-12">
                        <p><b>Producto:</b> {{ item["producto"]["nombre"] }} | <b>Precio unitario:</b> {{
                          item["producto"]["precio"] }} |
                          <b>Cantidad pedida:</b> {{ item["cantidad"] }}
                        </p>
                      </div>
                    </li>
                  </div>
                </ul>
                <div class="text-center pt-5">
                  <p class="fs-1 mb-5">Incluye número de pedido, productos solicitados, cantidad, precio unitario y
                    total</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import axios from "axios";
export default {
  name: "DetallePedido",
  data() {
    return {
      datosPedido: {},
    };
  },
  methods: {
    getPedidos() {
      axios({
        url:
          "http://127.0.0.1:8000/productopedido/" +
          this.$route.params.id +
          "/det/",
        headers: { Authorization: "Token " + this.$store.getters.getToken },
        method: "GET",
      }).then((response) => {
        this.datosPedido = response.data;
      });
    },
  },
  mounted() {
    this.getPedidos();
  },
};
</script>

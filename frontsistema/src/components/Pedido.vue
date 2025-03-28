<template>
  <section id="services" Style="background-image:url(assets/img/gallery/bg.png)">
      <div class="container">
        <div class="row h-100 justify-content-center">
          <div class="col-md-6 col-lg-5 col-xl-4">
            <div class="card h-100 px-lg-5 card-span">
              <div class="card-body d-flex flex-column justify-content-around">
                <div class="text-center pt-5">
                  <img class="img-fluid" src="assets/img/icons/services-2.svg" alt="..." />
                  <h3 class="my-4">Pedidos</h3>
                  <button v-on:click="crearPedido()" class="btn btn-success" type="button">
                    Crear nuevo pedido
                  </button>
                  <ul class="list-unstyled">
                    <li v-for="item in datosPedido" :key="item.id">
                      <div class="row">
                        <div class="col-12 col-sm-12 fs-2 fs-l-7">
                          <b>Código:</b> {{ item.id }} | <b>Fecha:</b> {{ item.fecha }} |
                          <b>Total:</b> {{ item.total }}
                          <span v-if="item.estado === 'A'">
                            <button v-on:click="cerrarPedido(item.id)" class="btn btn-outline-danger" type="button"
                              data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false"
                              aria-controls="collapseExample">
                              Cerrar pedido
                            </button>
                          </span>

                          <span v-else-if="item.estado === 'P'">
                            <button class="btn btn-warning" type="button" data-bs-toggle="collapse"
                              data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample"
                              disabled>
                              Pendiente
                            </button>
                          </span>
                          <span v-else-if="item.estado === 'V'">
                            <button class="btn btn-info" type="button" data-bs-toggle="collapse"
                              data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample"
                              disabled>
                              En viaje
                            </button>
                          </span>
                          <span v-else-if="item.estado === 'E'">
                            <button class="btn btn-success" type="button" data-bs-toggle="collapse"
                              data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample"
                              disabled>
                              Entregado
                            </button>
                          </span>
                          <router-link :to="'/detallepedido/' + item.id">
                            <button class="btn btn-outline-info" type="button" data-bs-toggle="collapse "
                              data-bs-target="#detPedido">
                              Ver detalle
                            </button>
                          </router-link>
                        </div>
                      </div>
                    </li>
                  </ul>
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
  //////
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Pedido",
  data() {
    return {
      datosPedido: {},
    };
  },
  ///////
  methods: {
    getPedidos() {
      axios({
        url: "http://127.0.0.1:8000/pedido/",
        headers: { Authorization: "Token " + this.$store.getters.getToken },
        method: "GET",
      }).then((response) => {
        this.datosPedido = response.data;
        const size = this.datosPedido.length;
        for (var i = 0; i < size; i++) {
          if (this.datosPedido[i].estado === "A") {
            this.$store.commit("cargarPedidoAbierto", this.datosPedido[i].id);
          }
        }
        console.log(this.$store.getters.getIdPedidoAbierto)
      });
    },
    cerrarPedido(idPedido) {
      axios({
        url: "http://127.0.0.1:8000/pedido/" + idPedido + "/",
        headers: { Authorization: "Token " + this.$store.getters.getToken },
        method: "PATCH",
        data: { estado: "P" },
      }).then(() => {
        this.$store.commit("sacarPedidoAbierto");
        this.getPedidos();
      });
    },
    crearPedido() {
      axios({
        url: "http://127.0.0.1:8000/pedido/crear/",
        headers: { Authorization: "Token " + this.$store.getters.getToken },
        method: "GET",
      }).then((response) => {
        this.$store.commit("cargarPedidoAbierto", response.data[0].id);
        console.log(response.data[0].id)
        this.getPedidos();
      });
    },
  },
  mounted() {
    this.getPedidos();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

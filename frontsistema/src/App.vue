<template>

  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3 d-block"
      data-navbar-on-scroll="data-navbar-on-scroll">
      <div class="container"><a class="navbar-brand" href="index.html"><img src="assets/img/gallery/logo.png"
            height="45" alt="logo" /></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span
            class="navbar-toggler-icon"> </span></button>
        <div class="collapse navbar-collapse border-top border-lg-0 mt-4 mt-lg-0" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto pt-2 pt-lg-0 font-base">
            <li>
              <router-link class="nav-item px-2" aria-current="page" to="/"><button type="button"
                  class="btn btn-outline-dark">Home</button></router-link>
            </li>
            <li>
              <router-link class="nav-item px-2" aria-current="page" to="/producto"><button type="button"
                  class="btn btn-outline-dark">Productos</button></router-link>
            </li>
            <span v-if="!isLogged">
              <li>
                <router-link class="nav-item px-2" aria-current="page" to="/login"><button type="button"
                    class="btn btn-outline-dark">Login</button></router-link>
              </li>
            </span>
            <span v-if="!isLogged">
              <li>
                <router-link class="nav-item px-2" aria-current="page" to="/registrar"><button type="button"
                    class="btn btn-outline-danger">Registrarse</button></router-link>
              </li>
            </span>
            <span v-if="isLogged">
              <li>
                <router-link class="nav-item px-2" aria-current="page" to="/pedido"><button type="button"
                    class="btn btn-outline-dark">Pedidos</button></router-link>
              </li>
            </span>
            <span v-if="isLogged">
              <li>
                <router-link class="nav-item px-2" aria-current="page" to="/logout"><button type="button"
                    class="btn btn-outline-danger">Salir</button></router-link>
              </li>
            </span>
          </ul>
        </div>
      </div>
    </nav>
    <div class="container-fluid"> <router-view />
    </div>
  </div>


</template>

<script>
export default {
  name: "App",
  computed: {
    isLogged() {
      return this.$store.getters.getIsLog;
    },
  },
};
</script>

<style></style>

<template>
  <Navbar />
  <router-view />
  <FooterSite />
</template>
  

<script>
import Navbar from '@/components/Navbar.vue';
import FooterSite from '@/components/Footer.vue'
import 'bootstrap/dist/css/bootstrap.min.css'


export default {
  name: 'App',
  components: {
    Navbar, FooterSite
  },
  watch: {
    $route() {
      this.$store.dispatch("onStart")
    }
  },
  mounted() {
    this.$store.dispatch("onStart")
  }
}
</script>



<style>
#app {
  font-family: "IRANSans", sans-serif;
}

body {
  background-color: #FCF6F5FF !important;
}
</style>

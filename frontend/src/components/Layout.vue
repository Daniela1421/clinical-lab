<template>
  <div>
    <b-navbar variant="light" type="light" class="mb-4" style="background-color: #e3f2fd;">
      <b-container>
        <b-navbar-brand href="#">🧪 Laboratorio clínico</b-navbar-brand>
        <b-navbar-nav>
          <b-nav-item to="/">Registrar Paciente</b-nav-item>
          <b-nav-item to="/orden">Crear Orden</b-nav-item>
          <b-nav-item to="/historial">Ver Historial</b-nav-item>
        </b-navbar-nav>
      </b-container>
    </b-navbar>

    <b-container>
      <router-view />
    </b-container>
  </div>
</template>

<script setup>
</script>

<template>
  <b-card title="Registrar Paciente" class="mb-4">
    <b-form @submit.prevent="registrarPaciente">
      <b-form-group label="Nombre Completo">
        <b-form-input v-model="paciente.nombre_completo" required />
      </b-form-group>

      <b-form-group label="Documento">
        <b-form-input v-model="paciente.documento" required />
      </b-form-group>

      <b-form-group label="Fecha de nacimiento">
        <b-form-input type="date" v-model="paciente.fecha_nacimiento" required />
      </b-form-group>

      <b-form-group label="Género">
        <b-form-select v-model="paciente.genero" :options="['Masculino', 'Femenino', 'Otro']" required />
      </b-form-group>

      <b-button type="submit" variant="primary">Registrar</b-button>
    </b-form>
  </b-card>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

const paciente = ref({
  nombre_completo: '',
  documento: '',
  fecha_nacimiento: '',
  genero: ''
})

const registrarPaciente = async () => {
  try {
    await axios.post('http://localhost:8000/pacientes/', paciente.value)
    alert('Paciente registrado')
  } catch (error) {
    alert('Error al registrar')
  }
}
</script>



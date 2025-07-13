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
      <p v-if="mensaje" :style="{ color: mensajeColor, marginTop: '1rem' }">
        {{ mensaje }}
      </p>
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

const mensaje = ref('')
const mensajeColor = ref('green')

const registrarPaciente = async () => {
  const soloNumeros = /^[0-9]+$/
  if (!soloNumeros.test(paciente.value.documento)) {
    mensaje.value = 'El documento debe contener solo números'
    mensajeColor.value = 'red'
    return
  }

  try {
    await axios.post('http://localhost:8000/pacientes/', paciente.value)
    mensaje.value = 'Paciente registrado exitosamente'
    mensajeColor.value = 'green'
    limpiarFormulario()
  } catch (error) {
    mensaje.value = 'Error al registrar paciente'
    mensajeColor.value = 'red'
  }
}

const limpiarFormulario = () => {
  paciente.value = {
    nombre_completo: '',
    documento: '',
    fecha_nacimiento: '',
    genero: ''
  }
}
</script>



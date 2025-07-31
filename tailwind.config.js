/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/templates/**/*.html', // Memindai semua file HTML di dalam folder templates
  ],
  // Daftarkan kelas-kelas dinamis di sini agar Tailwind selalu menyertakannya
  safelist: [
    'bg-green-50',
    'text-green-800',
    'bg-red-50',
    'text-red-800',
    'bg-blue-50', // Untuk kategori 'info'
    'text-blue-800', // Untuk kategori 'info'
    'bg-yellow-50', // Untuk kategori 'warning'
    'text-yellow-800', // Untuk kategori 'warning'
  ],
  theme: {
    extend: {
      fontFamily: {
        // Menjadikan 'Inter' sebagai font utama
        sans: ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
}

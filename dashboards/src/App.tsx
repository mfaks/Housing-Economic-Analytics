import { Header, DashboardTabs, Footer } from "./components"

function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <div className="container mx-auto p-6 flex-1">
        <Header />
        <DashboardTabs />
      </div>
      <Footer />
    </div>
  )
}

export default App
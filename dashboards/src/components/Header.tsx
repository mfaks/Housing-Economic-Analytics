import { LastUpdated } from "./LastUpdated"

export function Header() {
  return (
    <>
      <header className="mb-16 text-center">
        <h1 className="scroll-m-20 text-center text-4xl font-extrabold tracking-tight text-balance underline decoration-primary decoration-2">
          Housing Economic Analytics
        </h1>
      </header>
      <div className="text-center">
        <h2 className="scroll-m-20 pb-2 text-3xl font-medium tracking-tight first:mt-0">
          Interactive dashboards using data from the Federal Reserve and US Census Bureau.
          <br />
          Covers trends across economics, demographics, and housing.
        </h2>
      </div>
      <LastUpdated />
    </>
  )
}
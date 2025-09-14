import { Clock, Calendar } from "lucide-react"

export function LastUpdated() {

  const now = new Date()
  const lastUpdated = new Date(now.getFullYear(), now.getMonth(), 1)
  const nextUpdate = new Date(now.getFullYear(), now.getMonth() + 1, 1)

  const formatDate = (date: Date) => {
    return date.toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
      year: "numeric"
    })
  }

  return (
    <div className="flex items-center justify-center" style={{ gap: '32px' }}>
      <div className="flex items-center underline decoration-primary decoration-2">
        <Clock className="h-4 w-4 mr-2" />
        <h3 className="scroll-m-20 text-xl font-semibold tracking-tight first:mt-0">
          Last Updated: {formatDate(lastUpdated)}
        </h3>
      </div>
      <div className="flex items-center underline decoration-primary decoration-2">
        <Calendar className="h-4 w-4 mr-2" />
        <h3 className="scroll-m-20 text-xl font-semibold tracking-tight first:mt-0">
          Next Update: {formatDate(nextUpdate)}
        </h3>
      </div>
    </div>
  )
}
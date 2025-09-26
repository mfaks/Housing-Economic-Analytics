import type { ReactNode } from "react"
import type { LucideIcon } from "lucide-react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

interface DashboardCardProps {
  title: string
  icon: LucideIcon
  children: ReactNode
}

export function DashboardCard({ 
  title, 
  icon: Icon, 
  children
}: DashboardCardProps) {
  return (
    <Card>
      <CardHeader>
        <div className="flex items-center gap-3">
          <Icon className="h-6 w-6" />
          <CardTitle className="scroll-m-20 text-3xl font-semibold tracking-tight">
            {title}
          </CardTitle>
        </div>
      </CardHeader>
      <CardContent>
        <div className="aspect-video bg-muted rounded">
          {children}
        </div>
      </CardContent>
    </Card>
  )
}

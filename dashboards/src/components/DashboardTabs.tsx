import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs"
import { TrendingUp, Users, Home } from "lucide-react"

const dashboards = [
  { id: "economics", title: "Economics", icon: TrendingUp },
  { id: "demographics", title: "Demographics", icon: Users },
  { id: "housing", title: "Housing", icon: Home }
]

export function DashboardTabs() {
  return (
    <Tabs defaultValue="economics">
      <div className="flex justify-center mb-6">
        <TabsList className="grid grid-cols-3" style={{ width: '600px' }}>
          {dashboards.map((dashboard) => (
            <TabsTrigger key={dashboard.id} value={dashboard.id} style={{ fontSize: '18px', padding: '12px 24px' }}>
              {dashboard.title}
            </TabsTrigger>
          ))}
        </TabsList>
      </div>

      {dashboards.map((dashboard) => (
        <TabsContent key={dashboard.id} value={dashboard.id}>
            <div className="flex items-center justify-center h-full">
              <p className="text-lg leading-8 text-muted-foreground">Dashboard content coming soon</p>
            </div>
        </TabsContent>
      ))}
    </Tabs>
  )
}

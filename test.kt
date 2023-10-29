fun findByAppointment(appointmentId: String): List<ScheduleEntity> = list(
    "SELECT DISTINCT se " +
    "FROM ScheduleEntity se " +
    "JOIN ScheduleAssignmentEntity sa ON se.id = sa.schedule " +
    "JOIN AssignmentEntity a ON sa.assignment = a.id " +
    "AND a.appointmentId = :appointmentId",
    mapOf(
        "appointmentId" to appointmentId
    )
)

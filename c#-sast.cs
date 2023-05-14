        public string BlindWithHttpClient(string path)
        {
            string result = "Message was sent";

            HttpClient client = new HttpClient();

            try
            {
                HttpResponseMessage response = client.GetAsync(path).Result;
                var content = response.Content.ReadAsStringAsync().Result;
                client.Dispose();
            }
            catch (Exception e)
            {
                System.Diagnostics.Debug.WriteLine(e);
                result = "An error occured";
            }

            return result;
        }
        
        
        public string UnionBasedWithFormatString(string param)
        {
            string result = "";
            string query = String.Format("SELECT * from [dbo].[USER] WHERE NAME = '{0}';", param);

            try
            {
                using (SqlConnection connection = new SqlConnection(
                   GetConnectionString()))
                    {
                        connection.Open();

                        SqlCommand command = new SqlCommand(query, connection);
                        SqlDataReader reader = command.ExecuteReader();
                        while (reader.Read())
                        {
                            result += String.Format("Username: {0} Role: {1}", reader["NAME"], reader["ROLE"]);
                        }
                    }
            } catch(Exception e)
            {
                result = e.Message;
            }

            return result;
        }

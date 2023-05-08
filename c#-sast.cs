using RestSharp;
using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Text;

namespace DI.Services
{
    public class ServerSideRequestForgeryService : IServerSideRequestForgeryService
    {
        #region Classic

        public string ClassicWithHttpClient(string path)
        {
            string result = "";

            HttpClient client = new HttpClient();

            try
            {
                HttpResponseMessage response = client.GetAsync(path).Result;
                result = response.Content.ReadAsStringAsync().Result;
                client.Dispose();
            }
            catch (Exception e)
            {
                System.Diagnostics.Debug.WriteLine(e);
            }

            return result;
        }

        public string ClassicWithWebClient(string path)
        {
            string result = "";

            try
            {
                WebClient client = new WebClient();

                Stream data = client.OpenRead(path);
                StreamReader reader = new StreamReader(data);
                result = reader.ReadToEnd();
                client.Dispose();
            }
            catch (Exception e)
            {
                System.Diagnostics.Debug.WriteLine(e);
            }

            return result;
        }

        public string ClassicWithRestClient(string path)
        {
            string result = "";

            try
            {
                RestClient client = new RestClient(path);

                var request = new RestRequest("/");
                var response = client.Get(request);

                result = response.Content;
                
            }
            catch (Exception e)
            {
                System.Diagnostics.Debug.WriteLine(e);
            }

            return result;
        }
        #endregion
    }
}


using System;
using System.Diagnostics;

namespace DI.Services
{
    public class OsCommandInjectionService : IOsCommandInjectionService
    {
        #region Classic
        public string Classic(string command, string arguments)
        {
            string result = "";

            try
            {
                Process process = new Process();
                process.StartInfo.FileName = command;
                process.StartInfo.Arguments = arguments;
                process.StartInfo.UseShellExecute = false;
                process.StartInfo.RedirectStandardOutput = true;
                process.Start();

                result = process.StandardOutput.ReadToEnd();
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }

            return result;
        }

        public string ClassicWithProcessStartInfo(string command, string arguments)
        {
            string result = "";

            try
            {
                ProcessStartInfo processStartInfo = new ProcessStartInfo
                {
                    FileName = command,
                    Arguments = arguments,
                    UseShellExecute = false,
                    RedirectStandardOutput = true
                };

                var process = Process.Start(processStartInfo);
                result = process.StandardOutput.ReadToEnd();
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }

            return result;
        }

        public string Classic2(string ip)
        {
            string result = "";

            try
            {
                Process process = new Process();

                process.StartInfo.FileName = @"cmd.exe";
                process.StartInfo.Arguments = "/c ping " + ip;
                process.StartInfo.UseShellExecute = false;
                process.StartInfo.RedirectStandardOutput = true;
                process.Start();

                result = process.StandardOutput.ReadToEnd();
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }

            return result;
        }
        #endregion
    }
}



using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;

namespace DI.Services
{
    public class SqlInjectionService : ISqlInjectionService
    {
        private string GetConnectionString()
        {
            var connectionString = ConfigurationManager.ConnectionStrings["SqlExpress"].ConnectionString;

            return connectionString;
        }

        #region Union Based

        public string UnionBased(string param)
        {
            string result = "";
            string query = "SELECT * from [dbo].[USER] WHERE NAME = '" + param + "';";

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
        #endregion

        #region Error Based

        public string ErrorBased(string param)
        {
            string result;
            string query = "INSERT INTO [dbo].[PRODUCT] (NAME) VALUES ('" + param + "');";

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
                            System.Diagnostics.Debug.WriteLine(String.Format("{0}", reader[0]));
                        }
                    }

                result = "Product was added";

            } catch (Exception e)
            {
                result = e.Message;
            }

            return result;
        }

        public string ErrorBasedWithFormatString(string param)
        {
            string result;
            string query = String.Format("INSERT INTO [dbo].[PRODUCT] (NAME) VALUES ('{0}');", param);

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
                            System.Diagnostics.Debug.WriteLine(String.Format("{0}", reader[0]));
                        }
                    }

                result = "Product was added";

            } catch(Exception e)
            {
                result = e.Message;
            }

            return result;
        }
        #endregion
    }
}

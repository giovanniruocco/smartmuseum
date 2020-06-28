# EVALUATION

Project evaluation is a systematic and objective assessment of an ongoing or completed project. The aim is to determine the relevance and level of achievement of project objectives, development effectiveness, efficiency, impact and sustainability.  Evaluation assesses how well planning and managing for future impact is being done during the project cycle. To be useful, an evaluation must respond to the needs and interests of the users and provide information that facilitate decisions their making.

|Evaluation criteria                  |Description                          |
|-----------------------------|-------------------------------|
|`Relevance and strategic fit of the project` |The extent to which the objectives of a development intervention are consistent with beneficiary requirements, country needs, global priorities and partner and donor policies.|            
|`Validity of project design  ` |The extent to which the project design is logical and coherent.|
|`Main strategic components ` |The extent to which the project’s strategic components and how they logical link to the planned objectives.|
|`Survey ` |The extent to which feedback and idea the user can provide to the project. In that way they can be involved in project implementation. |            
|`Impact orientation and sustainability of the project.` |The strategic orientation of the project towards making a significant contribution to broader, long-term, sustainable development changes. The likelihood that the results of the project are durable and can be maintained or even scaled up and replicated by project partners after major assistance has been completed.  |
|`Risk analysis ` |The extent to which risks and assumptions the project logic build |
|`Effectiveness of management arrangements ` |The extent to which management capacities and arrangements put in place supports the achievement of results. |




# Evaluation of “Look at M.E.”

The idea of the project comes from relevant needs of different users. What came out from our first survey is that many times museums are scattered, and the way they store work arts makes the experience difficult. To help museum curators and visitors of “Museo dell’Arte Classica - Sapienza” we created “Look at M.E.”.  The strategic point of our project is the involvement by the user in a visual and sound experience that can change the point of view on the works of art.  After a careful analysis of the planimetry, we came to the conclusion that our project is feasible, in fact the implementation of boards with a proximity sensor, a button and a bluetooth module can be done without any problems. The museum, however, should provide speakers and lights capable of illuminating with a certain power the works of art involved in the experience.

From the user point of view, what stands out from the survey is that the experience sometimes can be a little invasive, in fact we can see from the chart below that the 39,1% of them believe that. Also, we can see that for several users the whole experience shouldn’t last longer than 10 minutes.

![Survey](https://github.com/giovanniruocco/smartmuseum/blob/master/images/Survey.PNG)
In the final state of the project, we will see the user reviews for the different rooms in the museum, paying attention to the impact of Look at M.E. by confronting the result of the rooms with and without Look at M.E.

Obviously, a risk analysis was done, since our hardware is not perfect. The accuracy of the motion sensor is not bad at all, but it can happen that in difficult situations a measurement can be wrong gave as result 0 caused by a board movement that made impossible for the receiver to get the reflected signal. As of now we addressed this issue by ignoring return values of zero for the publish to the broker. Regarding the lighting experience a latency problem might be on the activation of the button, in fact the experience sometimes can be delayed. Also the bluetooth sensor it's not perfect: it can happen that the connection between board an pc can be broken and we need to restart the board. Since we added a telegram bot there will be a problem if telegram goes down maybe for server down or unreachable because of a network problem, outage or a website maintenance in progress. Despite that, the data provided by the product in most cases are reliable and mqtt is responsive enough to manage different device and values with good results, so we can provide a comfortable user experience and reliable measurement to the museum curator.
